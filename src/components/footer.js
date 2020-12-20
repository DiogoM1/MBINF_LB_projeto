import React from "react"

const Footer = () => {
  return (
    <footer className="my-12 text-center">
      © {new Date().getFullYear()}, Construido com
      {` `}
      <a href="https://www.gatsbyjs.org">Gatsby</a> e o tema{" "}
      <a
        href="https://github.com/renyuanz/leonids"
        target="_blank"
        rel="noreferrer"
      >
        Leonids
      </a>
      . Análise por Angelina Eiras, Diogo Macedo e Pedro Borges, Mestrado em BioInfórmatica na Universidade do Minho
    </footer>
  )
}

export default Footer
