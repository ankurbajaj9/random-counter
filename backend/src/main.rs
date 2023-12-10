use async_std::sync::mpsc;
use async_std::net::TcpListener;
use async_std::net::TcpStream;
use rand::Rng;
use std::collections::HashMap;

struct RandomNumberGenerator {
    random_numbers: HashMap<usize, u32>,
    tx: mpsc::Sender<u32>,
    stats: HashMap<String, u32>,
}

impl RandomNumberGenerator {
    async fn new() -> Self {
        let random_numbers = HashMap::new();
        let (tx, rx) = mpsc::channel(1024);

        Self {
            random_numbers,
            tx,
            stats: HashMap::new(),
        }
    }

    async fn generate_random_numbers(self) {
        let mut rng = rand::thread_rng();

        loop {
            let random_number = rng.gen_range(1, 1001);
            let index = self.random_numbers.len();

            self.random_numbers.insert(index, random_number);

            self.update_stats(random_number);

            self.tx.send(random_number).await.unwrap();
        }
    }

    async fn get_stats(&self) -> HashMap<String, u32> {
        self.stats.clone()
    }

    fn update_stats(&mut self, random_number: u32) {
        let key = format!("{}", random_number);

        if self.stats.contains_key(&key) {
            self.stats[&key] += 1;
        } else {
            self.stats.insert(key, 1);
        }
    }
}