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

function Run-OCR($folder, $count) {
    Write-Host "================== $folder =================="
    for ($i = 1; $i -le $count; $i++) {
        $path = (Get-Item "assets/Fotos_Archivos/$folder/$i.png").FullName
        $file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($path))
        $stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read))
        $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream))
        $bmp = Await ($decoder.GetSoftwareBitmapAsync())
        $result = Await ($engine.RecognizeAsync($bmp))
        
        Write-Host "--- OBRA $i ($i.png) ---"
        Write-Host $result.Text
        Write-Host ""
    }
}

Run-OCR "Edicion_24" 9
Run-OCR "Edicion_25" 17
Run-OCR "Edicion_26" 14
