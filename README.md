# Aplikasi PKL SMK

Cloud Computing - PTI 2802
Pertemuan 3 - Project Inception

## Author
suryana / 25832074001 / PTI 2B

## Problem
Guru pembimbing dan siswa SMK mengalami kesulitan memantau pelaksanaan
praktik kerja lapangan (PKL) karena data penempatan, jurnal harian, dan
status kegiatan tersebar dan dicatat manual. Sistem menyediakan pencatatan
penempatan PKL, jurnal kegiatan, dan status pelaksanaan sehingga
perkembangan siswa dapat dipantau secara terpusat.

## Target Users
- Guru pembimbing PKL
- Siswa SMK peserta PKL
- Koordinator PKL sekolah

## Features M03
- Baseline application (halaman utama dengan daftar penempatan contoh)
- Health endpoint
- API info dan API penempatan
- VPS deployment

## Architecture

```mermaid
flowchart LR
    U[User] --> C[Caddy]
    C --> G[Gunicorn]
    G --> F[Flask]
```

Detail: `docs/architecture.md` dan `docs/adr/0001-initial-architecture.md`.

## Infrastructure
- Azure VM, Ubuntu Server 24.04 LTS
- 2 vCPU, sekitar 1 GB RAM, swap 1 GB
- Disk 64 GiB
- Caddy, Gunicorn, systemd, UFW

## Public Endpoint
`http://20.214.153.96/`

## Health Check
`GET /health`

## Deployment
Lihat `docs/deployment.md`.

## Security
- SSH key-only (Ed25519)
- Root SSH dan password SSH dinonaktifkan
- UFW aktif
- Backend loopback-only
- Tidak ada secret di repository

## Current Limitations
- HTTP only
- Data contoh tertulis di kode, belum ada database
- Tanpa container
- Deployment manual

## Roadmap
M04 DNS/HTTPS, M05 Data, M06 Container, M07 IaC, M09 CI/CD
