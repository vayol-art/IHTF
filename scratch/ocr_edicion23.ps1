Add-Type -AssemblyName System.Runtime.WindowsRuntime

$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | ? { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]

function Await($asyncOp) {
    $task = $asTaskGeneric.MakeGenericMethod($asyncOp.GetType().GetGenericArguments()[0]).Invoke($null, @($asyncOp))
    $task.Wait()
    return $task.Result
}

[void][Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics, ContentType = WindowsRuntime]
[void][Windows.Media.Ocr.OcrEngine, Windows.Foundation.Diagnostics, ContentType = WindowsRuntime]
[void][Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]

$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage([Windows.Globalization.Language]::new('en-US'))

for ($i = 1; $i -le 11; $i++) {
    $path = (Get-Item "assets/Fotos_Archivos/Edicion_23/$i.png").FullName
    $file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($path))
    $stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read))
    $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream))
    $bmp = Await ($decoder.GetSoftwareBitmapAsync())
    $result = Await ($engine.RecognizeAsync($bmp))
    
    Write-Host "=== OBRA $i ($i.png) ==="
    Write-Host $result.Text
    Write-Host "---------------------------------------------------`n"
}
