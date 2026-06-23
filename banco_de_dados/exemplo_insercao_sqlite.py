#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : exemplo_insercao_sqlite.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 10/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
        # con = self._conexao.conectar()
        # cursor = con.cursor()
        # cursor.execute("""INSERT INTO produto (
        #                          nome,
        #                          descricao,
        #                          codigo_barra,
        #                          preco_custo,
        #                          vendivel,
        #                          preco_venda,
        #                          categoria
        #            ) VALUES (?, ?, ?, ?, ?, ?, ?);""", (
        #                 produto.nome,
        #                 produto.descricao,
        #                 produto.codigo_barra,
        #                 produto.preco_custo,
        #                 produto.vendivel,
        #                 produto.preco_venda,
#                 produto.categoria
#             )
#            )
# con.commit()


# Outro Exemplo de inserção
    def salvar(self, produto: Produto):
        sql = """INSERT INTO produto (
                           nome,
                           descricao,
                           codigo_barra,
                           preco_custo,
                           vendivel,
                           preco_venda,
                           categoria
                           ) VALUES (?, ?, ?, ?, ?, ?, ?);"""
        with self._conexao.conectar() as con:
            cursor = con.cursor()
            cursor.execute(
                    sql,
                    (
                        produto.nome,
                        produto.descricao,
                        produto.codigo_barra,
                        produto.preco_custo,
                        produto.vendivel,
                        produto.preco_venda,
                        produto.categoria
                    )
            )
            con.commit()
