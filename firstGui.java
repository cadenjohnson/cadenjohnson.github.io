import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class firstGui implements ActionListener {
	
	// Initializing variable and objects
	private int count = 0;
	private JFrame frame;
	private JPanel panel;
	private JLabel label;
	
	public firstGui() {
		// Create frame and panel
		frame = new JFrame();
		panel = new JPanel();
		
		// Create button
		JButton button = new JButton("click here");
		button.addActionListener(this);
		label = new JLabel("number of clicks: 0");
		
		panel.setBorder(BorderFactory.createEmptyBorder(30,30,10,30));
		panel.setLayout(new GridLayout(0,1));
		
		panel.add(button);
		panel.add(label);
		
		frame.add(panel, BorderLayout.CENTER);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE );
		frame.setTitle("Caden's First GUI");
		frame.pack();
		frame.setVisible(true);
	}
	
	public static void main(String[] args) {
		new firstGui();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		count++;
		label.setText("number of clicks: " + count);
	}
}
