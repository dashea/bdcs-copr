Package of the dependencies of bdcs that are not already packages in Fedora

It's probably possible to automate these builds with the copr CLI, but on the
other hand that sounds like more work than it's worth. Here's the order to
build things in against F26:

* ![ghc-memory-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-memory-weldr/status_image/last_build.png) [ghc-memory-weldr](ghc-memory-weldr) (memory-0.14.7) 
* ![ghc-attoparsec-binary status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-attoparsec-binary/status_image/last_build.png) [ghc-attoparsec-binary](ghc-attoparsec-binary) 
* ![ghc-chunked-data status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-chunked-data/status_image/last_build.png) [ghc-chunked-data](ghc-chunked-data)
* ![ghc-vector-algorithms status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-vector-algorithms/status_image/last_build.png) [ghc-vector-algorithms](ghc-vector-algorithms)
* ![ghc-mono-traversable status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-mono-traversable/status_image/last_build.png) [ghc-mono-traversable](ghc-mono-traversable)
* ![ghc-conduit-combinators status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-conduit-combinators/status_image/last_build.png) [ghc-conduit-combinators](ghc-conduit-combinators)
* ![ghc-codec-rpm status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-codec-rpm/status_image/last_build.png) [ghc-codec-rpm](ghc-codec-rpm)
* ![ghc-cond status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-cond/status_image/last_build.png) [ghc-cond](ghc-cond)
* ![ghc-cpu status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-cpu/status_image/last_build.png) [ghc-cpu](ghc-cpu)
* ![ghc-cryptonite-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-cryptonite-weldr/status_image/last_build.png) [ghc-cryptonite-weldr](ghc-cryptonite-weldr)
* ![ghc-persistent status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-persistent/status_image/last_build.png) [ghc-persistent](ghc-persistent)
* ![ghc-esqueleto status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-esqueleto/status_image/last_build.png) [ghc-esqueleto](ghc-esqueleto)
* ![ghc-haskell-gi-base status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-haskell-gi-base/status_image/last_build.png) [ghc-haskell-gi-base](ghc-haskell-gi-base)
* ![ghc-haskell-gi status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-haskell-gi/status_image/last_build.png) [ghc-haskell-gi](ghc-haskell-gi)
* ![ghc-haskell-gi-overloading status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-haskell-gi-overloading/status_image/last_build.png) [ghc-haskell-gi-overloading](ghc-haskell-gi-overloading)
* ![ghc-gi-glib status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-glib/status_image/last_build.png) [ghc-gi-glib](ghc-gi-glib)
* ![ghc-gi-gobject status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-gobject/status_image/last_build.png) [ghc-gi-gobject](ghc-gi-gobject)
* ![ghc-gi-gio status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-gio/status_image/last_build.png) [ghc-gi-gio](ghc-gi-gio)
* ![ghc-gi-ostree status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-ostree/status_image/last_build.png) [ghc-gi-ostree](ghc-gi-ostree)
* ![ghc-gitrev-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gitrev-weldr/status_image/last_build.png) [ghc-gitrev-weldr](ghc-gitrev-weldr)
* ![ghc-asn1-types status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-asn1-types/status_image/last_build.png) [ghc-asn1-types](ghc-asn1-types)
* ![ghc-asn1-encoding status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-asn1-encoding/status_image/last_build.png) [ghc-asn1-encoding](ghc-asn1-encoding)
* ![ghc-asn1-parse status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-asn1-parse/status_image/last_build.png) [ghc-asn1-parse](ghc-asn1-parse)
* ![ghc-x509 status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-x509/status_image/last_build.png) [ghc-x509](ghc-x509)
* ![ghc-x509-store status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-x509-store/status_image/last_build.png) [ghc-x509-store](ghc-x509-store)
* ![ghc-x509-validation status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-x509-validation/status_image/last_build.png) [ghc-x509-validation](ghc-x509-validation)
* ![ghc-x509-system status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-x509-system/status_image/last_build.png) [ghc-x509-system](ghc-x509-system)
* ![ghc-tls status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-tls/status_image/last_build.png) [ghc-tls](ghc-tls)
* ![ghc-connection status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-connection/status_image/last_build.png) [ghc-connection](ghc-connection)
* ![ghc-http-client-tls status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-http-client-tls/status_image/last_build.png) [ghc-http-client-tls](ghc-http-client-tls)
* ![ghc-http-conduit status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-http-conduit/status_image/last_build.png) [ghc-http-conduit](ghc-http-conduit)
* ![ghc-parsec-numbers status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-parsec-numbers/status_image/last_build.png) [ghc-parsec-numbers](ghc-parsec-numbers)
* ![ghc-persistent-sqlite status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-persistent-sqlite/status_image/last_build.png) [ghc-persistent-sqlite](ghc-persistent-sqlite)
* ![ghc-persistent-template status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-persistent-template/status_image/last_build.png) [ghc-persistent-template](ghc-persistent-template)
* ![ghc-hspec-expectations status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-hspec-expectations/status_image/last_build.png) [ghc-hspec-expectations](ghc-hspec-expectations)
* ![ghc-quickcheck-io status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-quickcheck-io/status_image/last_build.png) [ghc-quickcheck-io](ghc-quickcheck-io)
* ![ghc-hspec-core status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-hspec-core/status_image/last_build.png) [ghc-hspec-core](ghc-hspec-core)
* ![ghc-hspec-discover status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-hspec-discover/status_image/last_build.png) [ghc-hspec-discover](ghc-hspec-discover)
* ![ghc-hspec status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-hspec/status_image/last_build.png) [ghc-hspec](ghc-hspec)
* ![libgit2 status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/libgit2/status_image/last_build.png) [libgit2](libgit2)
* ![libgit2-glib status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/libgit2-glib/status_image/last_build.png) [libgit2-glib](libgit2-glib)
* ![ghc-gi-ggit status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-gi-ggit/status_image/last_build.png) [ghc-gi-ggit](ghc-gi-ggit)
* ![ghc-htoml status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-htoml/status_image/last_build.png) [ghc-htoml](ghc-htoml)
* ![ghc-distributive-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-distributive-weldr/status_image/last_build.png) [ghc-distributive-weldr](ghc-distributive-weldr)
* ![ghc-comonad-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-comonad-weldr/status_image/last_build.png) [ghc-comonad-weldr](ghc-comonad-weldr)
* ![ghc-bifunctors status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-bifunctors/status_image/last_build.png) [ghc-bifunctors](ghc-bifunctors)
* ![ghc-semigroupoids status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-semigroupoids/status_image/last_build.png) [ghc-semigroupoids](ghc-semigroupoids)
* ![ghc-profunctors status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-profunctors/status_image/last_build.png) [ghc-profunctors](ghc-profunctors)
* ![ghc-free status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-free/status_image/last_build.png) [ghc-free](ghc-free)
* ![ghc-adjunctions status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-adjunctions/status_image/last_build.png) [ghc-adjunctions](ghc-adjunctions)
* ![ghc-kan-extensions status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-kan-extensions/status_image/last_build.png) [ghc-kan-extensions](ghc-kan-extensions)
* ![ghc-lens status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-lens/status_image/last_build.png) [ghc-lens](ghc-lens)
* ![ghc-lens-aeson status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-lens-aeson/status_image/last_build.png) [ghc-lens-aeson](ghc-lens-aeson)
* ![ghc-semver status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-semver/status_image/last_build.png) [ghc-semver](ghc-semver)
* ![ghc-crypto-pubkey-types](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-crypto-pubkey-types/status_image/last_build.png) [ghc-crypto-pubkey-types](ghc-crypto-pubkey-types)
* ![ghc-RSA](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-RSA/status_image/last_build.png) [ghc-RSA](ghc-RSA)
* ![ghc-authenticate-oauth status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-authenticate-oauth/status_image/last_build.png) [ghc-authenticate-oauth](ghc-authenticate-oauth)
* ![ghc-psqueues-weldr status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-psqueues-weldr/status_image/last_build.png) [ghc-psqueues-weldr](ghc-psqueues-weldr)
* ![ghc-wreq status](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-wreq/status_image/last_build.png) [ghc-wreq](ghc-wreq)
* ![ghc-unbounded-delays](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-unbounded-delays/status_image/last_build.png) [ghc-unbounded-delays](ghc-unbounded-delays)
* ![ghc-concurrent-extra](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-concurrent-extra/status_image/last_build.png) [ghc-concurrent-extra](ghc-concurrent-extra)
* ![ghc-generics-sop](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-generics-sop/status_image/last_build.png) [ghc-generics-sop](ghc-generics-sop)
* ![ghc-http-media](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-http-media/status_image/last_build.png) [ghc-http-media](ghc-http-media)
* ![ghc-natural-transformation](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-natural-transformation/status_image/last_build.png) [ghc-natural-transformation](ghc-natural-transformation)
* ![ghc-string-conversions](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-string-conversions/status_image/last_build.png) [ghc-string-conversions](ghc-string-converions)
* ![ghc-servant](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-servant/status_image/last_build.png) [ghc-servant](ghc-servant)
* ![ghc-servant-client](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-servant-client/status_image/last_build.png) [ghc-servant-client](ghc-servant-client)
* ![ghc-servant-foreign](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-servant-foreign/status_image/last_build.png) [ghc-servant-foreign](ghc-servant-foreign)
* ![ghc-servant-server](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-servant-server/status_image/last_build.png) [ghc-servant-server](ghc-servant-server)
* ![ghc-servant-options](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-servant-options/status_image/last_build.png) [ghc-servant-options](ghc-servant-options)
* ![ghc-wai-cors](https://copr.fedorainfracloud.org/coprs/g/weldr/bdcs-haskell-deps/package/ghc-wai-cors/status_image/last_build.png) [ghc-wai-cors](ghc-wai-cors)

Fedora 27 already has a sufficiently new version of libgit2.

Rawhide has the following packages:
  * ghc-bifunctors
  * ghc-esqueleto
  * ghc-persistent
  * ghc-persistent-sqlite
  * ghc-persistent-template
  * new enough libgit2
  * comonad with non-busted dependencies

Rawhide has a sufficiently new version of ghc-cryptonite, but build -weldr
anyway to relink against ghc-memory-weldr.
