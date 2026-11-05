param([string]$File, [double]$Start, [double]$Dur, [double]$Fps = 2, [int]$Cols = 8, [string]$Out)
$rows = [math]::Ceiling($Dur * $Fps / $Cols)
$vf = "fps=$Fps,scale=200:356:force_original_aspect_ratio=decrease,pad=200:356:(ow-iw)/2:(oh-ih)/2,drawtext=text='%{pts\:flt\:$Start}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.7,tile=${Cols}x${rows}"
ffmpeg -hide_banner -loglevel error -y -ss $Start -t $Dur -i $File -vf $vf -frames:v 1 $Out 2>$null
