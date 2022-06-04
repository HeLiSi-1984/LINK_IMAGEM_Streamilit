
import streamlit as st


def main():
    st.title("SITE PARA ANÁLISE DE JOGOS DE FUTEBOL")
    st.success('Para mercado de cantos e gols, ⬇️Só aqui você é green . ⬇️')
    L_imagem = 'https://i.postimg.cc/bvSWpw7S/HELISI-Bet-Bot.png'
    L_site = 'https://bit.ly/3t24BpR'

    ''' __Link com imagem ____________________'''
    st.markdown(f'''<p> CLIQUE AQUI ---> <a href="{L_site}"><img src="{L_imagem}" widht="400" height="250"></p>''', unsafe_allow_html=True)


    '''__Passado como um letreiro ___________________________________________'''
    st.markdown(
        f'''<h3><MARQUEE BEHAVIOR="alternate" DIRECTION="RIGHT" scrollamount="10" BGCOLOR="green" WIDTH=100% >
         <a href="{L_site}"><img src="{L_imagem}" width="300" height="270" "></MARQUEE></h3>''',
        unsafe_allow_html=True)


    '''___Pulando igual doido rsss __________________________________________'''
    st.markdown(f'''
    <marquee direction="down" width="1000" height="500" behavior="alternate" style="border:solid" scrollamount= "20">
    <marquee behavior="alternate"><a href="{L_site}"><img src="{L_imagem}" width="500" height="300" ">''',
     unsafe_allow_html=True)

if __name__ == '__main__':
    st.set_page_config(page_title= 'Image link', layout="wide")
    main()