{{/*
Expand the name of the chart.
*/}}
{{- define "random.random.name" -}}
{{- default .Chart.Name .Values.random.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- define "random.user.name" -}}
{{- default .Chart.Name .Values.user.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "random.random.fullname" -}}
{{- if .Values.random.fullnameOverride }}
{{- .Values.random.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.random.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}
{{- define "random.user.fullname" -}}
{{- if .Values.user.fullnameOverride }}
{{- .Values.user.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.user.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}


{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "random.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "random.labels" -}}
helm.sh/chart: {{ include "random.chart" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "random.random.selectorLabels" -}}
app.kubernetes.io/name: {{ include "random.random.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
{{- define "random.user.selectorLabels" -}}
app.kubernetes.io/name: {{ include "random.user.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "random.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "random.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
