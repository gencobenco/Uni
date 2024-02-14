Mehrere Mailboxen machen:
Add-PSSnapin *exchange*

$NumberOfMailboxes = 3

$Password = Read-Host "Geben Sie das Passwort ein" -AsSecureString

for ($i=1; $i -le $NumberOfMailboxes; $i++)
{
    $DisplayName = "Benutzer $i"

    $Alias = "GEERO$i"

    $EmailAddress = "GEERO_TST$i@test.pure-enterprise-cloud.de"

    New-Mailbox -Name $DisplayName -DisplayName $DisplayName -Alias $Alias -UserPrincipalName $EmailAddress -Password $Password
}
____________________________________________________________________
Mehrere Mailboxen löschen:

Add-PSSnapin *exchange*

$NumberOfMailboxes = 3

for ($i=1; $i -le $NumberOfMailboxes; $i++)
{
    $DisplayName = "Benutzer $i"

    $Alias = "GEERO$i"

    $EmailAddress = "GEERO_TST$i@test.pure-enterprise-cloud.de"

    Remove-Mailbox GEERO1 -Confirm -Force -IgnoreLegalHold 

}