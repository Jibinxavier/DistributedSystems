package controllers

import javax.inject.{Inject, Singleton}
import play.api.mvc.{AbstractController, ControllerComponents}


class AuthenticationController @Inject()(cc: ControllerComponents) extends AbstractController(cc) {



  def signUp = Action {
    Ok(views.html.index("Here's your sign up page"))
  }

  def login = Action {
    Ok(views.html.index("Here's your LOGin page"))
  }

}
