# Voz en off: solo recorta silencios y sube el volumen parejo. La voz queda natural.
# Sin EQ, sin compresor, sin limitador y sin reducción de ruido (regla de METODOLOGIA.md § 7.1).
#
# Uso (desde la carpeta del proyecto):
#   powershell -ExecutionPolicy Bypass -File ..\..\tools\voice.ps1 -In "..\..\<Modelo>\voz.m4a" -Segs "0.44-3.46,3.64-6.05,..."
#
# -Segs: tramos del audio original que se conservan (inicio-fin en segundos, separados por comas):
#   sin el silencio inicial y con cada pausa de más de 0,3 s acortada a ~0,1 s.
#   Se sacan de: ffmpeg -i <voz> -af silencedetect=noise=-38dB:d=0.12 -f null NUL
#   Sin -Segs se usa el audio completo.
# Nivel: ganancia lineal hasta -16 LUFS, pero sin pasar de -1 dBFS de pico (manda lo que llegue primero).
param(
  [Parameter(Mandatory = $true)][string]$In,
  [string]$Segs = "",
  [string]$Out = "assets\voz.wav"
)

# ($tramos y no $segs: PowerShell no distingue mayúsculas y pisaría el parámetro -Segs)
$tramos = New-Object System.Collections.ArrayList
if ($Segs) {
  foreach ($t in $Segs.Split(',')) { $p = $t.Trim().Split('-'); [void]$tramos.Add(@([double]$p[0], [double]$p[1])) }
} else {
  $d = [double](ffprobe -v error -show_entries format=duration -of csv=p=0 $In)
  [void]$tramos.Add(@(0.0, $d))
}

$n = $tramos.Count
$fc = "[0:a]aresample=48000,asplit=$n"
for ($i = 0; $i -lt $n; $i++) { $fc += "[r$i]" }
$fc += ";"
for ($i = 0; $i -lt $n; $i++) {
  $a = $tramos[$i][0]; $b = $tramos[$i][1]
  $d = [math]::Round($b - $a, 3)
  $fc += "[r$i]atrim=${a}:${b},asetpts=PTS-STARTPTS,afade=t=in:d=0.015,afade=t=out:st=$([math]::Round($d - 0.02, 3)):d=0.02[s$i];"
}
$fc += ($(0..($n - 1) | ForEach-Object { "[s$_]" }) -join "") + "concat=n=${n}:v=0:a=1[out]"

$tmp = "$Out.tmp.wav"
ffmpeg -hide_banner -loglevel error -y -i $In -filter_complex $fc -map "[out]" -ac 1 -c:a pcm_s24le $tmp

$o = ffmpeg -hide_banner -nostats -i $tmp -af "ebur128=peak=sample" -f null NUL 2>&1 | ForEach-Object { "$_" }
$I = [double](($o | Select-String "^\s+I:\s+(-?[\d\.]+) LUFS" | Select-Object -Last 1).Matches[0].Groups[1].Value)
$P = [double](($o | Select-String "^\s+Peak:\s+(-?[\d\.]+) dBFS" | Select-Object -Last 1).Matches[0].Groups[1].Value)
$gain = [math]::Round([math]::Min(-16 - $I, -1 - $P), 2)
ffmpeg -hide_banner -loglevel error -y -i $tmp -af "volume=${gain}dB" -ac 2 -c:a pcm_s16le $Out
Remove-Item $tmp
Write-Output "voz: $I LUFS, pico $P dBFS -> +$gain dB -> $Out"
