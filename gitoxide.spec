sources:
 - https://github.com/Byron/gitoxide
parts:
- uses: rust
  features:
  - fast
  - pretty-cli
  - http-client-reqwest
  - gitoxide-core-tools-query
  - gitoxide-core-tools
  - gitoxide-core-blocking-client
  - prodash-render-line
  - prodash-render-tui
  -  prodash/render-line-autoconfigure
  - gix/regex
  artifacts:
  - ein
  - gix
