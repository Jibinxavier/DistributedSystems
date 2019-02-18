package models

import cats.effect.IO
import tsec.cipher.symmetric._
import tsec.cipher.symmetric.jca._
import tsec.common._



class User(userName: String, password: String){


  def toJsonString(): String ={
    "userName:" +this.userName +",password:"+ this.password
  }

}
