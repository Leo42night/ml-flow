# Project
Dicoding - Membangun Sistem Machine Learning

## Requireq mlflow
- Up To GDrvie: service account
- Secret:
  - username (github)
  - email (github)
  - GDRIVE_CREDENTIALS
  - GDRIVE_FOLDER_ID

## Command
Activate Conda Env
```bash
conda activate credit_scoring
```
Run Server (server harus run jika ini menjalankan mlflow yang track URI)

```bash
mlflow server --host 127.0.0.1 --port 5000
```
## Track URI
(in other tab, also env active) Run modelling code
```bash
python modelling.py
```
```bash
python modellingopt.py
```
## In Github Action
Using `MLproject/` and `./github/workflows/config.yaml`. Sebelup push ke Github, cek jalankan di local (folder `mlruns/` akan dibuat):
```bash
mlflow run MLproject --env-manager=local
```
!WARNING!: jangan jalankan `mlflow server`, tracking URI akan meminta valid http or https dan akan error:
```bash
mlflow.exceptions.MlflowException: When an mlflow-artifacts URI was supplied, the tracking URI must be a valid http or https URI, but it was currently set to file:///C:
```
Cek `config.yaml` dan lakukan:
- Masukkan `secret` yang dibutuhkan ke setingan di Github Repo. 
- Pastikan nama branch sama dengan yang ada di repo. 
- Hilangkan `/mlruns` di `.gitignore` karena folder dibutuhkan untuk proses simpan GA.
Jika sudah, bisa push ke repo masing-masing dan cek hasilnya.

## Update Log
Handle waring di **modelling.py & modellingopt.py** (mlflow 3.5.1)
```python
# (aft) 13 | ubah int64 jadi float64 tuk handle null
data = data.astype({col: "float64" for col in data.columns if data[col].dtype == "int64"}) 
# ~ 32 | depecrated parameter change name
artifact_path="model" -> name="model"
```
Keterangan:
  - **(aft) 13** (setelah line 13)
  - **~ 32** (sekitar line 32)