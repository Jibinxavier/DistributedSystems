name := "DistributedSystems"
 
version := "1.0" 
      
lazy val `distributedsystems` = (project in file(".")).enablePlugins(PlayScala)

resolvers += "scalaz-bintray" at "https://dl.bintray.com/scalaz/releases"
      
resolvers += "Akka Snapshot Repository" at "http://repo.akka.io/snapshots/"
      
scalaVersion := "2.12.2"

libraryDependencies ++= Seq( jdbc , ehcache , ws , specs2 % Test , guice )

unmanagedResourceDirectories in Test <+=  baseDirectory ( _ /"target/web/public/test" )  

val testPythonTask = TaskKey[Unit]("Userdatabase", "Run Python user API.")

val command = "python3 server.py"
val workingDirectory = new File("./database")

testPythonTask := {
  val s: TaskStreams = streams.value
  s.log.info("Executing task Userdatabase")
  Process(command) ! s.log
}
val tsecV = "0.0.1-M11"
libraryDependencies ++= Seq(
  "io.github.jmcardon" %% "tsec-common" % tsecV,
  "io.github.jmcardon" %% "tsec-password" % tsecV,
  "io.github.jmcardon" %% "tsec-cipher-jca" % tsecV,
  "io.github.jmcardon" %% "tsec-cipher-bouncy" % tsecV,
  "io.github.jmcardon" %% "tsec-mac" % tsecV,
  "io.github.jmcardon" %% "tsec-signatures" % tsecV,
  "io.github.jmcardon" %% "tsec-hash-jca" % tsecV,
  "io.github.jmcardon" %% "tsec-hash-bouncy" % tsecV,
  "io.github.jmcardon" %% "tsec-libsodium" % tsecV,
  "io.github.jmcardon" %% "tsec-jwt-mac" % tsecV,
  "io.github.jmcardon" %% "tsec-jwt-sig" % tsecV,
  "io.github.jmcardon" %% "tsec-http4s" % tsecV
)