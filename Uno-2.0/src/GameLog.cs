using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class GameLog : MonoBehaviour {

    public GameObject logJogador1;
    private Text log1;
    static public string message1;

    public GameObject logJogador2;
    private Text log2;
    static public string message2;

    public GameObject logJogador3;
    private Text log3;
    static public string message3;

    // Use this for initialization
    void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
        log1 = logJogador1.GetComponent<Text>();
        log1.text = message1;

        log2 = logJogador2.GetComponent<Text>();
        log2.text = message2;

        log3 = logJogador3.GetComponent<Text>();
        log3.text = message3;
    }
}
