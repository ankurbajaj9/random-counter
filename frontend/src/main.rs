use async_std::net::TcpListener;
use async_std::net::TcpStream;
use async_std::sync::mpsc::Receiver;
use std::collections::HashMap;

async fn serve_random_numbers_ui(random_numbers: Receiver<u32>,) {
    let listener = TcpListener::bind("0.0.0.0:3000").await.unwrap();

    loop {
        let (stream, _) = listener.accept().await.unwrap();

        task::spawn(async move {
            let mut reader = async_std::io::BufReader::new(stream);
            let mut writer = async_std::io::BufWriter::new(stream);

            loop {
                let message = reader.readline().await.unwrap();

                if message == "GET\n" {
                    let stats = random_numbers.receiver().recv().await.unwrap();

                    for (statistic, value) in stats.iter() {
                        writer.write_all(format!("{}: {}\n", statistic, value).as_bytes()).await.unwrap();
                    }
                } else if message == "POST\n" {
                    let random_number = random_numbers.receiver().recv().await.unwrap();

                    writer.write_all(format!("Generated random number: {}\n", random_number).as_bytes()).await.unwrap();
                }
            }
        });
    }
}