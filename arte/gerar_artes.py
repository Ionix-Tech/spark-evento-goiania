# Gera as variações de formato da arte do evento a partir de arte.html.
# Cada formato só sobrescreve as medidas que mudam — o desenho é o mesmo.
import io, os, subprocess, sys
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

FORMATOS = {
    # nome            largura altura  css extra
    'feed-4x5':  (1080, 1350, ""),

    'quadrada-1x1': (1080, 1080, """
      .topo{ padding:60px 60px 0; }
      .eyebrow{ font-size:15px; }
      h1{ margin-top:32px; max-width:530px; font-size:66px; }
      .sub{ margin-top:24px; max-width:350px; font-size:22px; }
      .foto{ right:-32px; bottom:170px; width:505px; }
      .pe{ height:250px; }
      .rodape{ left:60px; right:60px; bottom:50px; }
      .rodape .rule{ margin-bottom:20px; }
      .rule{ width:72px; height:3px; }
      .rotulo{ font-size:13px; }
      .nome{ font-size:38px; }
      .pessoas{ gap:42px; padding-bottom:32px; }
      .mediador .nome{ font-size:23px; }
      .infos{ gap:48px; padding-bottom:28px; }
      .info svg{ width:26px; height:26px; }
      .info .rotulo{ font-size:11px; }
      .info .valor{ font-size:20px; }
      .creditos{ padding-top:24px; gap:52px; }
      .credito .rotulo{ font-size:11px; }
      .marcas{ margin-top:12px; gap:24px; }
      .m-ganplo{ height:24px; } .m-ionix{ height:21px; } .m-hub{ height:30px; }
      .barra{ height:10px; }
    """),

    'story-9x16': (1080, 1920, """
      .topo{ padding:200px 84px 0; }
      .eyebrow{ font-size:19px; }
      h1{ margin-top:46px; max-width:720px; font-size:92px; }
      .sub{ margin-top:34px; max-width:470px; font-size:30px; }
      .foto{ right:-46px; bottom:330px; width:720px; }
      .pe{ height:420px; }
      .glow-a{ top:300px; }
      .rodape{ left:84px; right:84px; bottom:150px; }
      .rodape .rule{ margin-bottom:30px; }
      .nome{ font-size:54px; }
      .pessoas{ gap:70px; padding-bottom:46px; }
      .mediador .nome{ font-size:31px; }
      .infos{ gap:72px; padding-bottom:40px; }
      .info .valor{ font-size:27px; }
      .creditos{ padding-top:36px; }
      .m-ganplo{ height:34px; } .m-ionix{ height:30px; } .m-hub{ height:42px; }
    """),
}

base = io.open(os.path.join(BASE, 'arte.html'), encoding='utf-8').read()

for nome, (w, h, extra) in FORMATOS.items():
    html = base.replace('width:1080px; height:1350px;', 'width:%dpx; height:%dpx;' % (w, h))
    if extra:
        html = html.replace('</style>', extra + '\n</style>')
    tmp = os.path.join(BASE, '_fmt_%s.html' % nome)
    io.open(tmp, 'w', encoding='utf-8').write(html)

    if '--html-only' in sys.argv:
        print('%-14s %dx%d  HTML preparado' % (nome, w, h))
        continue

    png = os.path.join(BASE, '_fmt_%s.png' % nome)
    subprocess.run([CHROME, '--headless', '--disable-gpu', '--hide-scrollbars',
                    '--virtual-time-budget=9000', '--window-size=%d,%d' % (w, h),
                    '--screenshot=' + png, 'file:///' + tmp.replace('\\', '/')],
                   capture_output=True)

    jpg = os.path.join(BASE, 'arte-%s.jpg' % nome)
    Image.open(png).convert('RGB').save(jpg, quality=92, optimize=True, progressive=True)
    print('%-14s %dx%d  %.0f KB' % (nome, w, h, os.path.getsize(jpg)/1024))
