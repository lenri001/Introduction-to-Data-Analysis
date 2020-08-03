/*
 * JMF Package
 * TCPClient
 * 
 * Simplified code for using TCP connections
 * 
 * AUTHOR: Joshua Frear
 * 
 * LAST MODIFIED: 
 * LAST MODIFIED BY: Joshua Frear
 * 
 * DO NOT MODIFY THIS CODE UNLESS DIRECTED BY THE AUTHOR
 */


import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class TCPClient {
	private String ip = null;
	private Integer port = null;
	
	private Socket sock = null;
	
	private DataOutputStream out = null;
	private DataInputStream in = null;
	
	private Boolean debugMode = false;
	static public String DEBUGFLAG = "-d";
	
	public TCPClient(String ip, Integer port) {
		// TODO Check correctness and return error for bad params
		this.ip = ip;
		this.port = port;
	}
			
	public void setDebugMode(Boolean b){
		System.out.println("TCPClient(" + ip + ") Debug Mode Set to\'" + b.toString() + "\'.");
		debugMode = b;
	}
	
	
	
	// TODO: public? private?
	public void printStatus(){
		printDebug("Client isConnected: " + sock.isConnected());
		printDebug("Client isClosed: " + sock.isClosed());
	}
	
	public void connect() throws IOException{
		printDebug("Connecting to " + ip + " on port " + port + ".");
		sock = new Socket(ip, port.intValue());
		
		OutputStream outToServer = sock.getOutputStream();
		out = new DataOutputStream(outToServer);
		
		InputStream inFromServer = sock.getInputStream();
		in = new DataInputStream(inFromServer);
		
		printDebug("Connected to " + sock.getRemoteSocketAddress() + ".");
		printStatus();
	}
	
	public void disconnect() throws IOException{
		System.out.println("Closing Connection...");
		sock.close();
		System.out.println("Connection is closed successfully.");
	}
	
	public void writeUTC(String message){
		try{
			printDebug("Sending message: \"" + message + "\" to client... ");
			out.writeUTF(message);
			printDebug("Message Sent!");
		}
		catch(IOException e){
			e.printStackTrace();
			System.exit(-1);
		}
	}
	
	public String readUTC(){
		String message = "<empty>";
		
		try{
			printDebug("Waiting for reply...");
			message = in.readUTF();
			printDebug("Server Response: " + message + "\n");
		}
		catch(IOException e){
			e.printStackTrace();
			System.exit(-1);
		}

		return message;
	}
	
	// Only prints messages if debug mode is set to true
	private void printDebug(String s){
		if(debugMode){
			System.out.println(s);
		}
	}
	
}