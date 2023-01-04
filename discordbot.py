from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")using Discord;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.DevTools.V106.WebAudio;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Runtime.Versioning;
using System.Text.RegularExpressions;
using System.Threading;

namespace DiscordBot
{
    public class AutoCharge
    {
        public static string[] Real = { "" };

        [SupportedOSPlatform("windows")]
        public static bool AutoChargeCode(string cookie, string code)
        {
            ChromeOptions options = new();
            options.AddExtension(Environment.CurrentDirectory + @"\Settings\cookie.crx");
            ChromeDriverService service = ChromeDriverService.CreateDefaultService();
            service.HideCommandPromptWindow = true;
            IWebDriver driver = new ChromeDriver(service, options)
            {
                Url = "chrome-extension://fngmhnnpilhplaeedifhccceomclgfbg/popup.html",
            };
            Thread.Sleep(500);
            driver.FindElement(By.XPath("/html/body/div[4]/div[3]/input")).Clear();
            driver.FindElement(By.XPath("/html/body/div[4]/div[3]/input")).SendKeys("https://m.cultureland.co.kr/mmb/loginMain.do");
            driver.FindElement(By.XPath("/html/body/div[4]/div[2]/div/a[6]")).Click();
            Thread.Sleep(500);
            driver.FindElement(By.XPath("/html/body/div[4]/div[9]/div/div/textarea")).SendKeys(cookie);
            driver.FindElement(By.XPath("/html/body/div[4]/div[11]/i")).Click();
            driver.Url = "https://m.cultureland.co.kr/csh/cshGiftCard.do";
            Thread.Sleep(500);
            try
            {
                driver.FindElement(By.Name("scr11")).SendKeys(code[..4]);
                driver.FindElement(By.Name("scr12")).SendKeys(code.Substring(4, 4));
                driver.FindElement(By.Name("scr13")).SendKeys(code.Substring(8, 4));
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[2]/a[1]")), "/html/body/div[2]/div[2]/a[1]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[2]/a[2]")),"/html/body/div[2]/div[2]/a[2]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[2]/a[3]")),"/html/body/div[2]/div[2]/a[3]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[2]/a[4]")),"/html/body/div[2]/div[2]/a[4]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[3]/a[1]")), "/html/body/div[2]/div[3]/a[1]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[3]/a[2]")),"/html/body/div[2]/div[3]/a[2]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[3]/a[3]")),"/html/body/div[2]/div[3]/a[3]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[3]/a[4]")),"/html/body/div[2]/div[3]/a[4]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[4]/a[1]")), "/html/body/div[2]/div[4]/a[1]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[4]/a[2]")),"/html/body/div[2]/div[4]/a[2]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[4]/a[3]")),"/html/body/div[2]/div[4]/a[3]");
                Screenshot(driver, driver.FindElement(By.XPath("/html/body/div[2]/div[4]/a[4]")), "/html/body/div[2]/div[4]/a[4]");
                driver.FindElement(By.XPath(Real[int.Parse(code.Substring(12, 1))])).Click();
                driver.FindElement(By.XPath("/html/body/div[1]/div[1]/form[2]/div[2]/input")).Click();
                return true;
            }
            catch
            {
                return false;
            }
        }
        [SupportedOSPlatform("windows")]
        public static void Screenshot(IWebDriver driver, IWebElement element, string xpath)
        {
            string[] files = Directory.GetFiles(Environment.CurrentDirectory + @"\Screenshot\Real\", "*.*", SearchOption.AllDirectories);
            foreach (var item in files)
            {
                Bitmap bitmap = new(Environment.CurrentDirectory + @"\Screenshot\Real\" + item);
                if (ImageCmp(Returnscreenshot(driver, element), bitmap) == true)
                {
                    Real[int.Parse(Regex.Replace(item, @"[^0-9]", ""))] = xpath;
                }
            }
        }

        [SupportedOSPlatform("windows")]
        public static Bitmap Returnscreenshot(IWebDriver driver, IWebElement element)
        {
            Byte[] byteArray = ((ITakesScreenshot)driver).GetScreenshot().AsByteArray;
            Bitmap screenshot = new(new System.IO.MemoryStream(byteArray));
            Rectangle croppedImage = new(element.Location.X, element.Location.Y, element.Size.Width, element.Size.Height);
            screenshot = screenshot.Clone(croppedImage, screenshot.PixelFormat);
            return screenshot;
        }
        [SupportedOSPlatform("windows")]
        public static void TakeScreenshot(IWebDriver driver, IWebElement element, string filename)
        {
            string fileName = filename + ".png";
            Byte[] byteArray = ((ITakesScreenshot)driver).GetScreenshot().AsByteArray;
            Bitmap screenshot = new(new System.IO.MemoryStream(byteArray));
            Rectangle croppedImage = new(element.Location.X, element.Location.Y, element.Size.Width, element.Size.Height);
            screenshot = screenshot.Clone(croppedImage, screenshot.PixelFormat);
            screenshot.Save(String.Format(Environment.CurrentDirectory + @"\Screenshot\" + fileName, ImageFormat.Png));
        }
        [SupportedOSPlatform("windows")]
        public static bool ImageCmp(Bitmap src, Bitmap bmp)
        {
            string srcInfo, bmpInfo;

            for (int i = 0; i < src.Width; i++)
            {
                for (int j = 0; j < src.Height; j++)
                {
                    srcInfo = src.GetPixel(i, j).ToString();
                    bmpInfo = bmp.GetPixel(i, j).ToString();

                    if (srcInfo != bmpInfo)
                    {
                        return false;
                    }
                }
            }
            return true;
        }
        public static string AutoCheck(string code)
        {
            if (code[..4].Contains("4180"))
            {
                ChromeOptions options = new();
                ChromeDriverService service = ChromeDriverService.CreateDefaultService();
                service.HideCommandPromptWindow = true;
                IWebDriver driver = new ChromeDriver(service, options)
                {
                    Url = "https://www.cultureland.co.kr/voucher/vouchercheck.do",
                };

                long.Parse(code);
                driver.FindElement(By.XPath("//*[@id=\"input-12\"]")).SendKeys(code[..4]);
                driver.FindElement(By.XPath("//*[@id=\"input-13\"]")).SendKeys(code.Substring(4, 4));
                driver.FindElement(By.XPath("//*[@id=\"input-14\"]")).SendKeys(code.Substring(8, 4));
                driver.FindElement(By.XPath("//*[@id=\"input-15\"]")).SendKeys(code.Substring(12, 4));
                driver.FindElement(By.XPath("/html/body/div[2]/div[2]/div[1]/div[3]/div/div[2]/dl/dd/div[2]/div/button")).Click();
                string money = driver.FindElement(By.XPath("/html/body/div[2]/div[2]/div[1]/div[3]/div/div[2]/dl/dd/p[2]/strong[3]")).Text;
                driver.Quit();
                if (money == "-")
                {
                    return "올바르지 않은 문화상품권 코드입니다.";
                }
                else
                {
                    return money + "원 충전 성공! (실제 충전까지 시간이 걸립니다)";
                }

            }
            else
            {
                return "올바르지 않은 문화상품권 코드입니다.";

            }
        }
    }
}
