# Evidence M03

- Platform: Azure VM (Korea Central), Ubuntu Server 24.04.5 LTS
- VM awalnya Ubuntu 22.04.5, di-upgrade ke 24.04 dengan do-release-upgrade
  setelah snapshot disk dibuat sebagai pengaman
- Public endpoint: http://20.214.153.96/
- Health: http://20.214.153.96/health

## Isi folder
- os.txt, resources.txt: spesifikasi sistem
- ufw.txt, ports.txt: firewall dan port yang listen
- service.txt: status service cc-m03
- health-internal.txt: health langsung ke Gunicorn (127.0.0.1:8000)
- health-public.txt: health lewat Caddy (127.0.0.1:80)
- ssh-hardening.txt: nilai efektif konfigurasi SSH
- Caddyfile.txt: konfigurasi reverse proxy

## Catatan
Screenshot browser dan portal Azure disimpan terpisah.
