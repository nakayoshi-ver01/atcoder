# AtCoder contest prep
# Usage: prep abc472
#        prep arc224

$global:AtCoderRoot = if ($PSScriptRoot) {
    $PSScriptRoot
} else {
    "C:\Users\nakay\OneDrive\デスクトップ\atcoder"
}

function global:prep {
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Contest
    )

    $root = $global:AtCoderRoot
    $contest = $Contest.Trim().ToLower()

    if ($contest -notmatch '^([a-z]+)') {
        Write-Error "Contest name must look like abc472 or arc224."
        return
    }

    $prefix = $Matches[1]
    $parent = Join-Path $root $prefix
    $dest = Join-Path $parent $contest
    $base = Join-Path $root "base_abc"

    if (-not (Test-Path -LiteralPath $base)) {
        Write-Error "Template not found: $base"
        return
    }

    New-Item -ItemType Directory -Force -Path $dest | Out-Null

    $created = 0
    $skipped = 0
    foreach ($file in (Get-ChildItem -LiteralPath $base -File)) {
        $newName = $file.Name -replace '^abc-', "$contest-"
        $destFile = Join-Path $dest $newName
        if (Test-Path -LiteralPath $destFile) {
            Write-Host "skip: $prefix/$contest/$newName"
            $skipped++
        } else {
            Copy-Item -LiteralPath $file.FullName -Destination $destFile
            Write-Host "create: $prefix/$contest/$newName"
            $created++
        }
    }

    Write-Host ("done: {0}  create={1} skip={2}" -f $dest, $created, $skipped)
    Set-Location -LiteralPath $dest
}

if ($args.Count -ge 1) {
    prep $args[0]
}