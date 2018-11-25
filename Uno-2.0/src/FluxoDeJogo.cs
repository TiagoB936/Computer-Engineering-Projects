using UnityEngine;
using System.Collections;

public class FluxoDeJogo : MonoBehaviour {

    static public int numJogador;
    static public int fluxo;

	// Use this for initialization
	void Start () {

        fluxo = 1;
        numJogador = 1;
	}

    // Update is called once per frame
    void Update()
    {
        vencedor();

    }

    static public void inverteFluxo()
    {
        fluxo *= (-1);
    }

    static public void proximo()
    {

        numJogador += fluxo;

        if(numJogador > 3)
        {
            numJogador = numJogador - 3;
        }
        if(numJogador < 1)
        {
            numJogador = numJogador + 3;
        }

        Debug.Log("Fluxo: " + fluxo);
        Debug.Log("Num Jogador: " + numJogador);
        //Debug.Log("Jogador 1 " + Jogador.cartas.Length);
        //Debug.Log("Jogador 2 " + NPC1.cartas.Length);
        //Debug.Log("Jogador 3 " + NPC2.cartas.Length);
    }

    void vencedor()
    {
        if(Jogador.cartas.Length < 1)
        {
            TelaDoVencedor.numVencedor = 1;
            Application.LoadLevel("Vencedor");
        }
        if (NPC1.cartas.Length < 1)
        {
            TelaDoVencedor.numVencedor = 2;
            Application.LoadLevel("Vencedor");
        }
        if (NPC2.cartas.Length < 1)
        {
            TelaDoVencedor.numVencedor = 3;
            Application.LoadLevel("Vencedor");
        }
    }
}
