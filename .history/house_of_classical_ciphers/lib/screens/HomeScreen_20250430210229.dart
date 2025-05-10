import 'package:flutter/material.dart';
import 'package:house_of_classical_ciphers/screens/CaesarScreen.dart';
import 'package:house_of_classical_ciphers/screens/atbash.dart';


class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  final List<String> algorithms = const [
    'Homophonic Cipher',
    'Atbash Cipher',
    'Playfair Cipher',
    'Affine Cipher',
    'Rail Fence Cipher',
    'Monoalphabetic Cipher',
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('House of Classical Ciphers'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: ListView.builder(
          itemCount: algorithms.length,
          itemBuilder: (context, index) {
            return Padding(
              padding: const EdgeInsets.symmetric(vertical: 10),
              child: ElevatedButton(
                onPressed: () {
                  Widget destinationPage;

                  switch (algorithms[index]) {
                    case 'Atbash Cipher':
                      destinationPage = const atbash();
                      break;
                    case 'Vigenère Cipher':
                      destinationPage = const VigenerePage();
                      break;
                    // case 'Playfair Cipher':
                    //   destinationPage = const PlayfairPage();
                    //   break;
                    // case 'Affine Cipher':
                    //   destinationPage = const AffinePage();
                    //   break;
                    // case 'Rail Fence Cipher':
                    //   destinationPage = const RailFencePage();
                    //   break;
                    // case 'Monoalphabetic Cipher':
                    //   destinationPage = const MonoalphabeticPage();
                    //   break;
                    default:
                      destinationPage = const Scaffold(
                        body: Center(child: Text('Coming Soon')),
                      );
                  }

                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => destinationPage),
                  );
                },
                style: ElevatedButton.styleFrom(
                  minimumSize: const Size(double.infinity, 50),
                  textStyle: const TextStyle(fontSize: 18),
                ),
                child: Text(algorithms[index]),
              ),
            );
          },
        ),
      ),
    );
  }
}
