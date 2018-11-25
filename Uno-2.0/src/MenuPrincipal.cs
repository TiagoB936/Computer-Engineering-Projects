using UnityEngine;
using System.Collections;

public class MenuPrincipal : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {

        if (Input.GetKeyUp(KeyCode.Return)) {
            TelaDoVencedor.numVencedor = 0;
            GameLog.message1 = " ";
            GameLog.message2 = " ";
            GameLog.message3 = " ";
            Application.LoadLevel("MesaDeJogo");

        }
        if (Input.GetKeyUp
            (KeyCode.Escape))
        {
            Application.Quit();
        }
	}
}
