import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;

public class basicLogin implements ActionListener{
	
	private JFrame frame;
	private JPanel panel;
	private static JLabel userLabel;
	private static JTextField usernameText;
	private static JLabel passLabel;
	private static JPasswordField passwordText;
	private static JButton button;
	public JLabel success;
	
	public basicLogin() {
		// Create frame and panel
		frame = new JFrame();
		panel = new JPanel();
		
		frame.add(panel, BorderLayout.CENTER);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE );
		frame.setTitle("Caden's Login GUI");
		frame.setSize(350, 200);
		
		panel.setBorder(BorderFactory.createEmptyBorder(30,30,10,30));
		panel.setLayout(null);
		
		// Create user name label and text input
		userLabel = new JLabel("Username");
		// (x,y,width,height)
		userLabel.setBounds(10, 20, 80, 25);
		panel.add(userLabel);
		
		usernameText = new JTextField();
		usernameText.setBounds(100, 20, 165, 25);
		panel.add(usernameText);
		
		// Create password label and text input
		passLabel = new JLabel("Password");
		passLabel.setBounds(10, 50, 80, 25);
		panel.add(passLabel);
		
		passwordText = new JPasswordField();
		passwordText.setBounds(100, 50, 165, 25);
		panel.add(passwordText);
		
		// Create login button
		button = new JButton("Login");
		button.setBounds(140, 80, 80, 25);
		button.addActionListener(this);
		panel.add(button);
		
		// Update panel with success message
		success = new JLabel("");
		success.setBounds(10,110, 300, 25);
		panel.add(success);
		
		frame.setVisible(true);
	}
	
	public static void main(String[] args) {
		// Create new instance of login page
		new basicLogin();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		// Retrieve user name and password
		String username = usernameText.getText();
		String password  = passwordText.getText();
		
		// Check if the user name and password are valid
		if(username.equals("admin") && password.equals("admin")) {
			success.setText("Welcome "+username+"!");;
		}
		else {
			success.setText("Login Failed");;
		}
		frame.setVisible(true);	
	}
}
