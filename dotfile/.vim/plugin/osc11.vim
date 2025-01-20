if exists('g:loaded_detectterm_bg')
  finish
endif
let g:loaded_detectterm_bg = 1

function! s:set_bg_by_brightness(r, g, b) abort
  let l:brightness = (a:r * 0.299) + (a:g * 0.587) + (a:b * 0.114)
  if l:brightness > 128
    set background=light
  else
    set background=dark
  endif
endfunction

function! s:UpdateBackgroundFromTermColor() abort
  if !exists('v:termrbgresp') || empty(v:termrbgresp)
    return
  endif

  let l:resp = v:termrbgresp

  let l:rgb_parts = matchlist(l:resp, 'rgb:\([0-9a-fA-F][0-9a-fA-F]\)[0-9a-fA-F][0-9a-fA-F]/\([0-9a-fA-F][0-9a-fA-F]\)[0-9a-fA-F][0-9a-fA-F]/\([0-9a-fA-F][0-9a-fA-F]\)[0-9a-fA-F][0-9a-fA-F]')
  if len(l:rgb_parts) >= 4
    let l:r = str2nr(l:rgb_parts[1], 16)
    let l:g = str2nr(l:rgb_parts[2], 16)
    let l:b = str2nr(l:rgb_parts[3], 16)

    call s:set_bg_by_brightness(l:r, l:g, l:b)
  endif
endfunction

" Buggy...
autocmd VimEnter * call echoraw(&t_RB)
" Debian 12 vim does not support TermResponseAll, you have to comment it out
" and manually call DetectTermBG.
autocmd TermResponseAll * call s:UpdateBackgroundFromTermColor()

command! DetectTermBG call s:UpdateBackgroundFromTermColor()
command! QueryTermBG call echoraw(&t_RB)
