class ShikiSyntaxHighlighter < Asciidoctor::SyntaxHighlighter::Base
  register_for 'shiki'

  def format node, lang, opts
    opts[:transform] = proc do |pre, code|
      code['class'] = %(language-#{lang}) if lang
    end
    super
  end

  def docinfo? location
    location == :footer
  end

  def docinfo location, doc, opts
    slash = opts[:self_closing_tag_slash]
    script = "
    shiki.getHighlighter({
      themes: ['min-light'],
      langs: ['python']
    }).then(highlighter => {
      document.querySelectorAll('.shiki').forEach(i => {
        const code = highlighter.codeToHtml(i.querySelector('code').innerText, 'python')
        i.innerHTML = code
      })
    })"
    %(<script src="https://cdn.jsdelivr.net/npm/shiki@0.9.10/dist/index.jsdelivr.iife.js"></script>
    <script>
      #{script}
    </script>)
  end
end