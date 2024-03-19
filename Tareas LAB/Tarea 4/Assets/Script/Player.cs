using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    public Rigidbody rb;
    public float speed = 5.0f;
    public int puntos = 0;
    // Start is called before the first frame update
    void Start()
    {
        rb = gameObject.GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        float movVertical = Input.GetAxis("Vertical");
        float movHorizontal = Input.GetAxis("Horizontal");
        Vector3 movimiento = new Vector3(movHorizontal, 0, movVertical);
        rb.AddForce(movimiento * speed);
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Punto")
        {
            puntos++;
            Destroy(other.gameObject);
        }

    }
}