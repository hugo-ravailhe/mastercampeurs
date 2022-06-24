import React from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
} from 'react-native';
import Logo from './Logo';

function DragDrop(props) {
  return (
    <View style={styles.container}>
      <Logo />
      <Text>Maintenant je suis là</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: '100%',
    height: '100%',
    backgroundColor: 'white',
  },
});

export default DragDrop;
