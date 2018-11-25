using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class TelaDoVencedor : MonoBehaviour {

    static public int numVencedor;

    public Image vencedor1;
    public Image vencedor2;
    public Image vencedor3;

    // Use this for initialization
    void Start () {
	    
        if(numVencedor == 0)
        {
            vencedor1.enabled = false;
            vencedor2.enabled = false;
            vencedor3.enabled = false;
        }
        if(numVencedor == 1)
        {
            vencedor1.enabled = true;
        }
        if(numVencedor == 2)
        {
            vencedor2.enabled = true;
        }
        if(numVencedor == 3)
        {
            vencedor3.enabled = true;
        }

	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
