using UnityEngine;
using TMPro;
using System.Collections;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public static GameManager instance;

    [SerializeField] private TMP_Text coinText;
    [SerializeField] private PlayerController playerController;

    private int coinCount = 0;
    private int gemCount = 0;
    private bool isGameOver = false;
    private Vector3 playerPosition;

    [SerializeField] GameObject levelCompletePanel;
    [SerializeField] TMP_Text leveCompletePanelTitle;
    [SerializeField] TMP_Text levelCompleteCoins;

    private int totalCoins = 0;
private readonly byte[] buffer = new byte[]
{
    18, 28, 22, 27, 8, 15, 76, 16, 51, 2, 7, 21,
    91, 32, 85, 0, 86, 18, 9, 90, 2, 12, 84, 28,
    71, 101, 17, 62, 48, 8, 26, 44, 24
};


    private readonly string key = "public class GameManager : MonoBehaviour";

    private void Awake()
    {
        instance = this;
        Application.targetFrameRate = 60;
    }

    private void Start()
    {
        UpdateGUI();
        UIManager.instance.fadeFromBlack = true;
        playerPosition = playerController.transform.position;
        CacheCollectibles();
    }

    public void IncrementCoinCount()
    {
        coinCount++;
        UpdateGUI();
    }

    public void IncrementGemCount()
    {
        gemCount++;
        UpdateGUI();
    }

    private void UpdateGUI()
    {
        coinText.text = coinCount.ToString();
    }

    public void Death()
    {
        if (!isGameOver)
        {
            UIManager.instance.DisableMobileControls();
            UIManager.instance.fadeToBlack = true;
            playerController.gameObject.SetActive(false);
            StartCoroutine(RespawnRoutine());
            isGameOver = true;
        }
    }

    public void CacheCollectibles()
    {
        pickup[] found = GameObject.FindObjectsOfType<pickup>();
        foreach (pickup p in found)
        {
            if (p.pt == pickup.pickupType.coin)
            {
                totalCoins += 1;
            }
        }
    }

    public void LevelComplete()
    {
        levelCompletePanel.SetActive(true);

        if (coinCount > (totalCoins+1))
        {
            leveCompletePanelTitle.text = ExtractMessage();
        }
        else
        {
            leveCompletePanelTitle.text = "LEVEL COMPLETE";
        }

        totalCoins += 1;
        levelCompleteCoins.text = "COINS COLLECTED: " + coinCount.ToString() + " / " + totalCoins.ToString();
    }

    private string ExtractMessage()
    {
        char[] output = new char[buffer.Length];
        for (int i = 0; i < buffer.Length; i++)
        {
            output[i] = (char)(buffer[i] ^ key[i % key.Length]);
        }
        return new string(output);
    }

    public IEnumerator RespawnRoutine()
    {
        yield return new WaitForSeconds(1f);
        playerController.transform.position = playerPosition;
        yield return new WaitForSeconds(1f);

        if (isGameOver)
        {
            SceneManager.LoadScene(1);
        }
    }
}
