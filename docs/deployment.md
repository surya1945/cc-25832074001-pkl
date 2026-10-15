# Manual Deployment M03

## Application Path
`/srv/cc-m03`

## Service
`cc-m03.service` (systemd, user `suryanaa`)

## Backend
`127.0.0.1:8000` (Gunicorn, 1 worker, 2 thread)

## Reverse Proxy
Caddy pada port 80, konfigurasi di `/etc/caddy/Caddyfile`:

```text
:80 {
    encode zstd gzip
    reverse_proxy 127.0.0.1:8000
}
```

## Public Endpoint
`http://20.214.153.96/`

## Health Check
`http://20.214.153.96/health`

## Network Layers
1. Azure Network Security Group: port 22 dan 80 diizinkan
2. UFW: OpenSSH dan 80/tcp diizinkan, default deny incoming
3. Caddy menerima request publik
4. Gunicorn hanya listen di loopback

## Update Procedure

```bash
cd /srv/cc-m03
git pull
source .venv/bin/activate
python -m pip install -r requirements.txt
sudo systemctl restart cc-m03
sudo systemctl status cc-m03 --no-pager
curl -fsS http://127.0.0.1:8000/health
curl -fsS http://127.0.0.1/health
```

## Rollback Dasar

```bash
cd /srv/cc-m03
git log --oneline --decorate -10
git checkout m03
sudo systemctl restart cc-m03
```

Kembali ke branch utama:

```bash
git switch main
```

## Troubleshooting Cepat
| Gejala | Kandidat utama |
|---|---|
| SSH bisa, HTTP timeout | Azure NSG / UFW / Caddy |
| HTTP 502 | Gunicorn / aplikasi |
| curl :8000 gagal | Gunicorn / Flask |
| curl :8000 berhasil, :80 gagal | Caddy |
| localhost berhasil, public gagal | NSG / firewall |
| aplikasi hilang setelah reboot | systemd enable / config |
