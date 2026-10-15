# Requirements

## Problem Statement
Guru pembimbing dan siswa SMK mengalami kesulitan memantau pelaksanaan
praktik kerja lapangan (PKL) karena data penempatan, jurnal harian, dan
status kegiatan tersebar dan dicatat manual.
Sistem menyediakan pencatatan penempatan PKL, jurnal kegiatan, dan status
pelaksanaan sehingga perkembangan siswa dapat dipantau dan ditelusuri
secara terpusat.

## Target Users
- Guru pembimbing PKL
- Siswa SMK peserta PKL
- Koordinator PKL sekolah

## User Needs
- Sebagai guru pembimbing, saya ingin melihat siswa yang belum mengisi
  jurnal PKL, sehingga saya dapat menindaklanjuti ketidakhadiran laporan.
- Sebagai siswa, saya ingin mencatat kegiatan harian PKL saya, sehingga
  laporan PKL tersusun rapi dan tidak terlewat.

## Functional Requirements
- FR-01 Sistem menampilkan halaman utama.
- FR-02 Sistem menyediakan health endpoint (`/health`).
- FR-03 Sistem menampilkan metadata aplikasi (`/api/info`).
- FR-04 Sistem menampilkan daftar penempatan PKL contoh (siswa, tempat,
  periode, status) pada halaman utama dan `/api/penempatan`.

## Non-Functional Requirements
- NFR-01 Backend hanya listen pada loopback (127.0.0.1:8000).
- NFR-02 Aplikasi dikelola systemd.
- NFR-03 Request publik masuk melalui reverse proxy (Caddy).
- NFR-04 Secret tidak disimpan pada Git repository.
- NFR-05 Health endpoint mengembalikan HTTP 200 saat sehat.
- NFR-06 Deployment dapat direproduksi dari repository.
- NFR-07 Arsitektur sesuai VPS kecil (sekitar 1 GB RAM).

## Constraints
- Azure Virtual Machine, Standard B2ats v2 (2 vCPU, sekitar 1 GB RAM)
- Disk 64 GiB (SSD Premium LRS)
- Ubuntu Server 24.04 LTS (upgrade dari 22.04 pada VM yang sama)
- Public IPv4

## Scope M03
In scope: repository, requirements, architecture, ADR, baseline Flask app,
SSH hardening dasar, Gunicorn, systemd, Caddy, HTTP publik.
Out of scope: database, Docker, IaC, CI/CD, TLS/domain, login dan form jurnal.

## Acceptance Criteria M03
- [x] first deployment accessible
- [x] health endpoint works
- [x] backend loopback-only
- [x] service managed by systemd
- [x] SSH key-only authentication
