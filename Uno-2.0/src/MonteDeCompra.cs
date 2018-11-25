using UnityEngine;
using System.Collections;

public class MonteDeCompra : MonoBehaviour {

    static public GameObject[] monteDeCompra;

	// Use this for initialization

    void Awake()
    {
        monteDeCompra = Resources.LoadAll<GameObject>("Cards");
        distribui();
        
    }

	void Start () {
    }
	
	// Update is called once per frame
	void Update () {
        

        if (PilhaPrincipal.pilhaPrincipal.Length < 4)
        {
            GameObject carta;

            for (int i = 0; i < 4 - PilhaPrincipal.pilhaPrincipal.Length; i++)
            {
                carta = remove();
                PilhaPrincipal.adiciona(carta);
            }

        }
        
    }

    static public GameObject remove()
    {
        GameObject carta;

        carta = monteDeCompra[0];

        for(int i = 0; i < monteDeCompra.Length - 1; i++)
        {
            monteDeCompra[i] = monteDeCompra[i + 1];
        }

        System.Array.Resize<GameObject>(ref monteDeCompra, monteDeCompra.Length - 1);

        return carta;
    }

    static public void adicionaEmbaixo(GameObject carta)
    {
        System.Array.Resize<GameObject>(ref monteDeCompra, monteDeCompra.Length + 1);

        monteDeCompra[monteDeCompra.Length - 1] = carta;

    }
    
    void distribui()
    {
        GameObject carta;

        embaralha(monteDeCompra);

        carta = remove();
        PilhaPrincipal.adiciona(carta);
        carta = remove();
        PilhaPrincipal.adiciona(carta);
        carta = remove();
        PilhaPrincipal.adiciona(carta);
        carta = remove();
        PilhaPrincipal.adiciona(carta);

        for (int i = 0; i < 7; i++)
        {
            carta = remove();
            Jogador.adiciona(carta);

            carta = remove();
            NPC1.adiciona(carta);
            carta = remove();

            NPC2.adiciona(carta);
        }
    }

    void embaralha(GameObject[] cartas)
    {
        for (int t = 0; t < cartas.Length; t++)
        {
            GameObject tmp = cartas[t];
            int r = Random.Range(t, cartas.Length);
            cartas[t] = cartas[r];
            cartas[r] = tmp;
        }
    }
}
