# Extrae cada toma de la lista (EDL) a 1080x1920, 30 fps, H.264 de alta calidad, con un grade suave.
#
# Uso (desde la carpeta del proyecto, ej. videos\nibosi-2628):
#   powershell -ExecutionPolicy Bypass -File ..\..\tools\extract-shots.ps1 -Src "..\..\Nibosi 2628" -Edl edl.csv
#   (opcional) -Only s07,s11   -> extrae solo esas tomas
#
# edl.csv (con encabezado):  id,archivo,entrada,duracion,4k
#   id        nombre de la toma (s01, s02...) -> assets\clips\<id>.mp4
#   archivo   nombre del video fuente sin extensión (IMG_1585) dentro de -Src (.MOV)
#   entrada   segundo de la fuente donde empieza la toma
#   duracion  segundos que dura en la línea de tiempo (se agregan 0,25 s de margen)
#   4k        1 = se extrae a 2160x3840 para hacerle un acercamiento fuerte sin perder nitidez
param(
  [Parameter(Mandatory = $true)][string]$Src,
  [string]$Edl = "edl.csv",
  [string]$Out = "assets\clips",
  [string[]]$Only = @()
)

New-Item -ItemType Directory -Force $Out | Out-Null
$grade = "eq=contrast=1.07:brightness=0.025:saturation=1.12:gamma=0.97,unsharp=5:5:0.35:5:5:0"

foreach ($e in Import-Csv $Edl) {
  if ($Only.Count -gt 0 -and $Only -notcontains $e.id) { continue }
  $dur = [math]::Round([double]$e.duracion + 0.25, 3)   # margen para que la toma nunca se quede sin cuadros
  $size = if ($e.'4k' -eq '1') { "2160:3840" } else { "1080:1920" }
  $file = Get-ChildItem -Path $Src -Filter "$($e.archivo).*" | Where-Object { $_.Extension -match '^\.(mov|mp4|m4v)$' } | Select-Object -First 1
  if (-not $file) { Write-Output "FALTA $($e.archivo) en $Src"; continue }
  ffmpeg -hide_banner -loglevel error -y -ss $e.entrada -i $file.FullName -t $dur -an `
    -vf "scale=${size}:flags=lanczos:force_original_aspect_ratio=increase,crop=${size},fps=30,$grade,format=yuv420p" `
    -c:v libx264 -preset slow -crf 12 -g 15 -colorspace bt709 -color_primaries bt709 -color_trc bt709 -movflags +faststart "$Out\$($e.id).mp4"
  Write-Output "$($e.id) <- $($e.archivo) @ $($e.entrada)s ($dur s) $size"
}
