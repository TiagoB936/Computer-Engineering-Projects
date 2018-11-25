using UnityEngine;
using System.Collections;

public class PilhaPrincipal : MonoBehaviour {

    static public GameObject[] pilhaPrincipal = new GameObject[0];
    static public GameObject cartaTopo;

    // Use this for initialization
    void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
        consertaMontes();
	}

    static public void adiciona(GameObject carta)
    {

        System.Array.Resize<GameObject>(ref pilhaPrincipal, pilhaPrincipal.Length + 1);

        for(int i = pilhaPrincipal.Length - 1; i > 0; i--)
        {
            pilhaPrincipal[i] = pilhaPrincipal[i - 1];
        }

        pilhaPrincipal[0] = carta;

        mostraTopo();
    }

    static public GameObject remove()
    {
        GameObject carta;

        carta = pilhaPrincipal[0];

        for(int i = 0; i < pilhaPrincipal.Length - 1; i++)
        {
            pilhaPrincipal[i] = pilhaPrincipal[i + 1];
        }

        System.Array.Resize<GameObject>(ref pilhaPrincipal, pilhaPrincipal.Length - 1);

        mostraTopo();

        return carta;
    }

    public static void mostraTopo()
    {
        Destroy(cartaTopo);

        cartaTopo = (GameObject)Instantiate(pilhaPrincipal[0]);
        
    }

    static public bool cartaEquivalente(float rot, string numero)
    {
        bool equivalente = false;

        if(rot == cartaTopo.gameObject.transform.rotation.z || numero == cartaTopo.gameObject.tag)
        {
            equivalente = true;
        }
        else
        {
            equivalente = false;
        }
        
        return equivalente;
    }

    void consertaMontes()
    {
        if (pilhaPrincipal.Length > 10)
        {
            GameObject cartaTemp;

            while(pilhaPrincipal.Length > 10)
            {
                cartaTemp = pilhaPrincipal[pilhaPrincipal.Length - 1];
                MonteDeCompra.adicionaEmbaixo(cartaTemp);
                System.Array.Resize<GameObject>(ref pilhaPrincipal, pilhaPrincipal.Length - 1);
            }
        }
    }
}
