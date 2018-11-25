using UnityEngine;
using System.Collections;

public class Jogador : MonoBehaviour {

    static public GameObject[] cartas = new GameObject[0];
    static public GameObject cartaTopo;

    // Use this for initialization
    void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
        mudaTopo();
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
        GameObject jogador = GameObject.FindGameObjectWithTag("jogador 1");

        Destroy(cartaTopo);

        cartaTopo = (GameObject)Instantiate(cartas[0], jogador.transform.position, cartas[0].gameObject.transform.rotation);

    }

    void mudaTopo()
    {

        if (Input.GetKeyUp(KeyCode.RightArrow))
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
}
