set number
syntax on
set nocompatible
" tab settings
set expandtab
set smarttab
set softtabstop=2
set tabstop=2
set shiftwidth=2

colorscheme elflord
highlight CursorLineNR ctermbg=red
" set cursorline
set mouse=a

if has("autocmd")
  au BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$")
    \| exe "normal! g'\"" | endif
endif

