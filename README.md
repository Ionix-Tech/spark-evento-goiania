# Spark — evento Goiânia (21/09)

Landing do evento presencial **"O que é hype e o que é real na IA?"** — palestra do
Oliver Cunningham no HUB Cerrado, Goiânia/GO, 21 de setembro, 09h. Realização
Ganplo · Ionix.

Reconstrução da landing anterior (`papaya-squirrel-5dc4d7.netlify.app`) na
**identidade visual canônica da Ionix**: violeta `#A855F7`, fundo `#0A0A0A`,
faixa gradient violeta→magenta→ciano, Montserrat + JetBrains Mono nos eyebrows.
O conteúdo é o mesmo da versão anterior — só o design mudou.

Página estática (HTML/CSS/JS vanilla, sem build), pra carregar rápido no wifi de evento.

## Estrutura

```
index.html    landing + modal de inscrição (Netlify Forms)
styles.css    identidade Ionix
assets/       arte do evento, retrato do palestrante, logos e favicons
arte/         fonte da arte do evento (HTML) + os formatos exportados
netlify.toml  config de deploy
```

## Arte do evento

A peça original (Ganplo) está preservada em `arte/original-ganplo.jpg`. A versão
em uso é refeita na identidade Ionix, com a foto real do Oliver recortada do
fundo de estúdio — `arte/oliver_arte.png`.

A arte é desenhada em HTML (`arte/arte.html`) e exportada com Chrome headless.
Para regerar os três formatos:

```
cd arte && python gerar_artes.py
```

Sai `arte-feed-4x5.jpg` (1080×1350, feed), `arte-quadrada-1x1.jpg` (1080×1080)
e `arte-story-9x16.jpg` (1080×1920, stories). O feed 4:5 é o que alimenta
`assets/evento-goiania.jpg` no hero da landing — ao trocar a arte, copiar o novo
export por cima desse arquivo.

Os logos Ganplo e HUB Cerrado foram extraídos da peça original (branco sobre
transparente). Se aparecerem os arquivos vetoriais, substituir
`arte/logo_ganplo.png` e `arte/logo_hubcerrado.png`.

## Deploy

```
netlify deploy --prod --dir=.
```

O formulário usa **Netlify Forms** (`data-netlify="true"`, name `inscricao-evento-goiania`).
O Netlify só registra o form no build do site — em deploy manual, conferir em
Site settings → Forms se `inscricao-evento-goiania` aparece na lista.

## Assets

- `evento-goiania.jpg` — arte oficial do evento (Ganplo)
- `oliver-cunningham.jpg` — foto real do Oliver, recorte 4:5 de
  `Ionix Tech/Marketing/Fotos Perfil Sócio/Oliver.jpeg` (Drive). A versão de
  origem tem 800×800; se aparecer o arquivo em alta da mesma sessão, refazer o
  crop a partir dele.
- `ionix-logo-dark.png` — logo Ionix negativo (fundo escuro)
- `ionix-logo-light.png` — logo Ionix positivo (fundo claro), não usado hoje
