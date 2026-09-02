-- Present top-level book section headings on two visual lines without changing
-- the canonical Markdown source. The header remains a single semantic H1 so
-- Pandoc can still generate a useful table of contents.
local function split_heading(text)
  local number, title = text:match('^Kapitel%s+(%d+)%s+–%s+(.+)$')
  if not number then number, title = text:match('^Kapitel%s+(%d+)%s+—%s+(.+)$') end
  if not number then number, title = text:match('^Kapitel%s+(%d+)%s+%-%s+(.+)$') end
  if number and title then return 'Kapitel ' .. number, title end

  local appendix, appendix_title = text:match('^(Bilaga%s+[%aÅÄÖåäö])%s+–%s+(.+)$')
  if not appendix then appendix, appendix_title = text:match('^(Bilaga%s+[%aÅÄÖåäö])%s+—%s+(.+)$') end
  if not appendix then appendix, appendix_title = text:match('^(Bilaga%s+[%aÅÄÖåäö])%s+%-%s+(.+)$') end
  if appendix and appendix_title then return appendix, appendix_title end

  local intro_title = text:match('^Inledning%s+–%s+(.+)$')
  if not intro_title then intro_title = text:match('^Inledning%s+—%s+(.+)$') end
  if not intro_title then intro_title = text:match('^Inledning%s+%-%s+(.+)$') end
  if intro_title then return 'Inledning', intro_title end

  return nil, nil
end

function Header(el)
  if el.level ~= 1 then
    return nil
  end

  local text = pandoc.utils.stringify(el.content)
  local label, title = split_heading(text)
  if not label or not title then
    return nil
  end

  local parsed = pandoc.read(title, 'markdown')
  local title_inlines = pandoc.Inlines{}
  if #parsed.blocks > 0 and parsed.blocks[1].content then
    title_inlines = parsed.blocks[1].content
  else
    title_inlines = pandoc.Inlines{pandoc.Str(title)}
  end

  el.content = pandoc.Inlines{
    pandoc.Span(pandoc.Inlines{pandoc.Str(label)}, pandoc.Attr('', {'chapter-number'})),
    pandoc.Span(pandoc.Inlines{pandoc.Str(' – ')}, pandoc.Attr('', {'chapter-separator'})),
    pandoc.Span(title_inlines, pandoc.Attr('', {'chapter-name'}))
  }
  return el
end
