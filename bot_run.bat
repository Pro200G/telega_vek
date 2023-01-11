@echo off

call %~dp0telega_vek\venv\Scripts\activate

cd %~dp0telega_vek

set TOKEN=5604489438:AAEQpf712li48y1PQDqCC1n8-w6ewgaxX78

python VEKART_bot.py

pause