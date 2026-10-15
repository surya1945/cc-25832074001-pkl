# ADR-0001: Initial VPS Deployment Architecture

## Status
Accepted

## Context
Proyek Aplikasi PKL SMK dideploy pada Azure VM (2 vCPU, sekitar 1 GB RAM,
disk 64 GiB, Ubuntu Server 24.04 LTS). VM dibuat dengan Ubuntu 22.04 lalu
di-upgrade ke 24.04 dengan do-release-upgrade setelah snapshot disk dibuat,
agar sesuai dengan referensi modul (Python 3.12).

## Decision
- Flask sebagai web framework
- Gunicorn dengan 1 worker dan 2 thread
- systemd sebagai service manager
- Caddy sebagai reverse proxy
- UFW sebagai host firewall
- GitHub sebagai remote repository dengan deploy key

## Alternatives
1. Node.js + PM2
2. NGINX + Gunicorn
3. Docker
4. PHP-FPM

## Rationale
- Python 3.12 adalah runtime default Ubuntu 24.04.
- Flask ringan dan cukup untuk baseline.
- Gunicorn pada loopback memperkecil attack surface.
- Caddy konfigurasinya sederhana dan siap dikembangkan menjadi HTTPS otomatis.
- Docker ditunda karena containerization adalah target M06.
- NGINX valid, tetapi Caddy dipilih karena konfigurasi lebih ringkas.

## Consequences
### Positive
- Footprint kecil, sesuai VM 1 GB.
- Arsitektur mudah dijelaskan dan diaudit.
- Jalur ke HTTPS (M04) sudah siap.
### Negative
- Deployment masih manual.
- Satu server tanpa redundansi.
- HTTP tanpa enkripsi pada M03.
- Upgrade in-place meninggalkan risiko sisa konfigurasi 22.04.

## Review Trigger
Review pada M06/M07.
