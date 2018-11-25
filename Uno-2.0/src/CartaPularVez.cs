using UnityEngine;
using System.Collections;

public class CartaPularVez : MonoBehaviour {

    public string numero;
    float rot; //substitui cor
    public string cor;
    int dono;

    // Use this for initialization
    void Start()
    {
        rot = this.gameObject.transform.rotation.z;
    }

    // Update is called once per frame
    void Update()
    {
        usarCarta();
        comprar();
    }

    void usarCarta()
    {
        if (FluxoDeJogo.numJogador == 1)
        {
            usarComoJogador();
        }
        if (FluxoDeJogo.numJogador == 2)
        {
            usarComoNPC1();
        }
        if (FluxoDeJogo.numJogador == 3)
        {
            usarComoNPC2();
        }
    }

    void comprar()
    {
        if (FluxoDeJogo.numJogador == 1)
        {
            if (Input.GetKeyUp(KeyCode.B))
            {
                GameObject cartaTemp;

                cartaTemp = MonteDeCompra.remove();
                Jogador.adiciona(cartaTemp);
                GameLog.message1 = "Jogador 1 : Comprou";
                FluxoDeJogo.proximo();
            }
        }
    }

    void OnTriggerEnter2D(Collider2D area)
    {
        if (area.gameObject.tag == "jogador 1")
        {
            dono = 1;
        }
        if (area.gameObject.tag == "jogador 2")
        {
            dono = 2;
        }
        if (area.gameObject.tag == "jogador 3")
        {
            dono = 3;
        }
    }

    void usarComoJogador()
    {
        if (Input.GetKeyUp(KeyCode.Return) && this.dono == FluxoDeJogo.numJogador)
        {

            if (PilhaPrincipal.cartaEquivalente(rot, numero))
            {
                GameObject cartaTemp;
                cartaTemp = Jogador.remove();
                PilhaPrincipal.adiciona(cartaTemp);
                GameLog.message1 = "Jogador 1 : " + numero + " " + cor;
                FluxoDeJogo.proximo();
                FluxoDeJogo.proximo();
            }

        }
    }

    void usarComoNPC1()
    {

        if (this.dono == FluxoDeJogo.numJogador)
        {
            if (PilhaPrincipal.cartaEquivalente(rot, numero))
            {
                GameObject cartaTemp;
                cartaTemp = NPC1.remove();
                PilhaPrincipal.adiciona(cartaTemp);
                GameLog.message2 = "Jogador 2 : " + numero + " " + cor;
                FluxoDeJogo.proximo();
                FluxoDeJogo.proximo();

                NPC1.mudancaDeTopo = 0;
            }
            else
            {
                NPC1.mudancaDeTopo++;
                NPC1.mudaTopo();
            }
        }
    }

    void usarComoNPC2()
    {
        if (this.dono == FluxoDeJogo.numJogador)
        {
            if (PilhaPrincipal.cartaEquivalente(rot, numero))
            {
                GameObject cartaTemp;
                cartaTemp = NPC2.remove();
                PilhaPrincipal.adiciona(cartaTemp);
                GameLog.message3 = "Jogador 3 : " + numero + " " + cor;
                FluxoDeJogo.proximo();
                FluxoDeJogo.proximo();

                NPC2.mudancaDeTopo = 0;
            }
            else
            {
                NPC2.mudancaDeTopo++;
                NPC2.mudaTopo();
            }
        }
    }
}
