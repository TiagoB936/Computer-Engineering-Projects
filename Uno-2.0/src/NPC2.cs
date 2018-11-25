using UnityEngine;
using System.Collections;

public class NPC2 : MonoBehaviour {

    static public GameObject[] cartas = new GameObject[0];
    static public GameObject cartaTopo;
    static public int mudancaDeTopo;

    // Use this for initialization
    void Start()
    {
        mudancaDeTopo = 0;
    }

    // Update is called once per frame
    void Update()
    {
        if (mudancaDeTopo == cartas.Length)
        {
            compra();
        }
    }

    static public void adiciona(GameObject carta)
    {
        System.Array.Resize<GameObject>(ref cartas, cartas.Length + 1);

        for (int i = cartas.Length - 1; i > 0; i--)
        {
            cartas[i] = cartas[i - 1];
        }

        cartas[0] = carta;

        mostraTopo();
    }

    static public GameObject remove()
    {
        GameObject carta;

        carta = cartas[0];

        for (int i = 0; i < cartas.Length - 1; i++)
        {
            cartas[i] = cartas[i + 1];
        }

        System.Array.Resize<GameObject>(ref cartas, cartas.Length - 1);

        mostraTopo();

        return carta;
    }

    public static void mostraTopo()
    {
        GameObject jogador = GameObject.FindGameObjectWithTag("jogador 3");

        Destroy(cartaTopo);

        cartaTopo = (GameObject)Instantiate(cartas[0], jogador.transform.position, cartas[0].gameObject.transform.rotation);

    }

    void compra()
    {
        GameObject cartaTemp;

        cartaTemp = MonteDeCompra.remove();
        adiciona(cartaTemp);
        mudancaDeTopo = 0;
        GameLog.message3 = "Jogador 3 : Comprou";
        FluxoDeJogo.proximo();

    }

    static public void mudaTopo()
    {
        GameObject cartaTemp;

        cartaTemp = cartas[0];

        for (int i = 0; i < cartas.Length - 1; i++)
        {
            cartas[i] = cartas[i + 1];
        }

        cartas[cartas.Length - 1] = cartaTemp;

        mostraTopo();
    }
}
