# AtCoder Workspace Setup Script
# このスクリプトを実行すると、現在のPowerShellセッションで便利なエイリアスが有効になります。

# 1. エイリアスの設定
function Setup-AtCoderAliases {
    # コンテストディレクトリ作成 (acc new [contest_id])
    Set-Alias -Name an -Value acc-new-wrapper -Option AllScope
    
    # テスト実行 (oj test)
    Set-Alias -Name t -Value oj-test-wrapper -Option AllScope
    
    # 提出 (acc submit)
    Set-Alias -Name s -Value acc-submit-wrapper -Option AllScope
}

function acc-new-wrapper {
    param($contest_id)
    if (-not $contest_id) { Write-Host "Usage: an [contest_id]" -ForegroundColor Red; return }
    acc new $contest_id
}

function oj-test-wrapper {
    $hasTests = (Test-Path .\tests) -or (Test-Path .\test)
    if (-not $hasTests) {
        Write-Host "Test directory not found. Please run 'oj d' or make sure you are in a task directory." -ForegroundColor Red
        return
    }

    if (Test-Path .\main.cpp) {
        Write-Host "Compiling main.cpp..." -ForegroundColor Cyan
        g++ -O3 -std=c++20 main.cpp -o main.exe
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Compilation failed." -ForegroundColor Red
            return
        }
        oj t -c ".\main.exe"
    } elseif (Test-Path .\main.py) {
        oj t -c "python main.py" -d tests
    } else {
        Write-Host "Neither main.cpp nor main.py found." -ForegroundColor Yellow
    }
}

function acc-submit-wrapper {
    if (Test-Path .\main.cpp) {
        acc s main.cpp
    } elseif (Test-Path .\main.py) {
        acc s main.py
    } else {
        Write-Host "Neither main.cpp nor main.py found." -ForegroundColor Yellow
    }
}

# 2. atcoder-cli の設定 (一度だけでOK)
function Configure-AtCoderCli {
    acc config default-test-dirname tests
    acc config default-task-choice all
    Write-Host "atcoder-cli configured." -ForegroundColor Green
}

Setup-AtCoderAliases
Write-Host "AtCoder aliases (an, t, s) are now active in this session." -ForegroundColor Cyan
Write-Host "Script auto-detects main.cpp or main.py for compilation, testing, and submission." -ForegroundColor Yellow
