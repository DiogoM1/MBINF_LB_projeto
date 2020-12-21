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
      . Código da análise em {` `}
      <a href="https://github.com/DiogoM1/MBINF_LB_projeto">MBINF LB Projeto</a>
    </footer>
  )
}

export default Footer
