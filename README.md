# Timelex: videos y proyectos de edición

Esta carpeta reúne las tomas originales, referencias, voces, música, guiones, videos exportados y proyectos HyperFrames de Timelex.

## Descargar todo en otra máquina

Instala Git y Git LFS. Luego abre una terminal en la carpeta donde quieras guardar el proyecto y ejecuta:

```powershell
git lfs install
git clone --depth 1 https://github.com/andresvielma-bit/timelex-vid.git
cd timelex-vid
git lfs pull
```

Los archivos MOV y MP4 se guardan en Git LFS para conservar su calidad original. Usa los comandos anteriores para descargar el contenido completo. El ZIP de GitHub puede contener solo referencias a esos archivos.

Si ya tienes el repositorio en la otra máquina, guarda tus cambios locales antes de actualizarlo:

```powershell
git lfs install
git switch main
git pull --ff-only
git lfs pull
```

## Continuar editando

Lee `AGENTS.md` y `METODOLOGIA.md`. Las carpetas con nombres de modelos contienen el material original y los videos exportados; `videos/` contiene los proyectos HyperFrames y sus recursos. Las herramientas y motores instalados en esta laptop se configuran por separado en la otra máquina.

GitHub incluye cuotas de almacenamiento y descarga para Git LFS. Consulta el uso de tu cuenta antes de subir nuevas tandas grandes: https://docs.github.com/en/billing/concepts/product-billing/git-lfs
