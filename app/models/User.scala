package models

import cats.effect.IO
import tsec.cipher.symmetric._
import tsec.cipher.symmetric.jca._
import tsec.common._



class User(userName: String, password: String){


  def toJsonString(): String ={
    "userName:" +this.userName +",password:"+ this.password
  }
  def encContent(): Unit ={
    implicit val ctrStrategy: IvGen[IO, AES128CTR] = AES128CTR.defaultIvStrategy[IO]
    implicit val cachedInstance: IO[Encryptor[IO, AES128CTR, SecretKey]] = AES128CTR.genEncryptor[IO] //Cache the implicit
    val toEncrypt: Array[Byte] = "hi hello welcome to tsec".utf8Bytes


    val onlyEncrypt: IO[String] =
      for {
        key       <- AES128CTR.generateKey[IO] //Generate our key
        encrypted <- AES128CTR.encrypt[IO](PlainText(toEncrypt), key) //Encrypt our message
        decrypted <- AES128CTR.decrypt[IO](encrypted, key)
      } yield decrypted.toUtf8String // "hi hello welcome to tsec!"


  }
}
