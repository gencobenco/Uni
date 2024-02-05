$farbe = Read-Host "Welche Farbe hat das Stopp-Schild?"

if($farbe -eq "rot") {
    Write-Host "Rot ist die richtige Farbe."
}
Else {
    Write-Host "Falsch. $farbe ist es nicht."
}
