package services

import java.security.MessageDigest
import java.util.Calendar

import javax.crypto.Cipher
import javax.crypto.spec.IvParameterSpec
import javax.crypto.spec.SecretKeySpec
import org.apache.commons.codec.binary.Base64
import org.bouncycastle.util.test.FixedSecureRandom.BigInteger
import play.api.Configuration

import scala.util.Random

//reference https://stackoverflow.com/questions/15554296/simple-java-aes-encrypt-decrypt-example
import javax.inject.{Inject}
class Encryption @Inject()( config: Configuration) {
    def encrypt(key: String, initVector: String, value: String ): String = {
      // add code depending on the data type
      try {
          val iv = new IvParameterSpec(initVector.getBytes("UTF-8"))
          val skeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES")
          val cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING")

          cipher.init(Cipher.DECRYPT_MODE, skeySpec, iv)
          val encrypted = cipher.doFinal(value.getBytes)

          System.out.println("encrypted string: " + Base64.encodeBase64String(encrypted))

          return Base64.encodeBase64String(encrypted)


      } catch {
        case ex: Exception =>
          ex.printStackTrace()
      }
      return ""


    }
  def randomKeyGenerator():String={
    val randomNumber = {Random.alphanumeric take 16 mkString}
    //println(" The random number is  " + randomNumber)
    return String.format("%032x", new BigInteger(1, MessageDigest.getInstance("SHA-256").digest(randomNumber.getBytes("UTF-8"))))
  }
  def decrypt(key: String, initVector: String, encrypted: String ): String = {

    try{
      val iv = new IvParameterSpec(initVector.getBytes("UTF-8"))
      val skeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES")
      val cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING")

      cipher.init(Cipher.DECRYPT_MODE, skeySpec, iv)
      val original = cipher.doFinal(Base64.decodeBase64(encrypted))
      return new String(original)


    }

    catch {
      case ex: Exception =>
        ex.printStackTrace()
    }
    return ""
  }

  def tokenGenerator(): Map[String,String] =  {
    // TODO get rid of this static randominitvector
    val initVector:String = "RandomInitVector"

    var sharedPass = config.get[String]("sharedKey")
    val sessionExpiryTM =  Calendar.getInstance().add(Calendar.HOUR, config.get[Int]("tokenLifeTimeInHours")).toString()
    val sessionExpiryTMEnc = encrypt(sharedPass,initVector, sessionExpiryTM)
    var sessionIdEnc = encrypt(sharedPass,initVector,randomKeyGenerator())
    Map("sessionId"->sessionIdEnc, "sessionExpiryTM"-> sessionExpiryTMEnc )

  }

}

// var key: String = "TestKey"
// val initVector:String = "RandomInitVector"
// println(Encryption.encrypt(key, initVector,"My very short stringHello"))
// println(Encryption.decrypt(key, initVector, Encryption.encrypt(key, initVector,"My very short stringHello"))